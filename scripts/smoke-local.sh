#!/usr/bin/env bash

set -euo pipefail
# script stops immediately if a command fails or an unset variable is used
# If a part of a pipeline fails, the entire pipeline is considered to have failed.

API_HEALTH_URL="${API_HEALTH_URL:-http://localhost:8000/api/v1/health}"
# if API_HEALTH_URL is not set, http://localhost:8000/api/v1/health should be used
WEB_URL="${WEB_URL:-http://localhost:3000}"
PROMETHEUS_URL="${PROMETHEUS_URL:-http://localhost:9090/-/ready}"
# /-/ready is a Prometheus endpoint that checks whether Prometheus is ready
GRAFANA_URL="${GRAFANA_URL:-http://localhost:3001/api/health}"

check_url() {
  local name="$1" # first argument
  local url="$2" # second argument

  echo "Checking ${name}: ${url}"

  if ! curl --fail --silent --show-error --max-time 10 "${url}" >/tmp/smoke-response.txt; then
    echo "Smoke check failed: ${name} is not reachable at ${url}"
    exit 1 # terminate script
  fi

  echo "OK: ${name}"
}

check_api_health() {
  echo "Checking API health: ${API_HEALTH_URL}"

  if ! curl --fail --silent --show-error --max-time 10 "${API_HEALTH_URL}" >/tmp/smoke-api-health.json; then
    echo "Smoke check failed: API health endpoint is not reachable at ${API_HEALTH_URL}"
    exit 1
  fi

  if ! grep -q '"status":"ok"' /tmp/smoke-api-health.json; then
  # searches for the text "status":"ok" in the JSON and should only return whether it was successfully found
    echo "Smoke check failed: API health endpoint did not return status ok"
    echo "Response:"
    cat /tmp/smoke-api-health.json
    exit 1
  fi

  echo "OK: API health"
}

echo "Running local smoke checks..."
echo # blank line

check_api_health
echo
check_url "Web app" "${WEB_URL}"
echo
check_url "Prometheus" "${PROMETHEUS_URL}"
echo
check_url "Grafana" "${GRAFANA_URL}"

echo
echo "All local smoke checks passed."
