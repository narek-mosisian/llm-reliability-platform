// web app home page

const platformFeatures = [
  "RAG with grounded citations",
  "LLM gateway with provider fallback",
  "Evaluation gates for AI quality",
  "OpenTelemetry, Prometheus and Grafana observability",
];

export default function HomePage() {
  return (
    <main className="page-shell">
      <section className="hero">
        <p className="eyebrow">LLM Reliability Platform</p>

        <h1>Production-grade reliability for RAG-based LLM applications.</h1>

        <p className="hero-copy">
          A focused AI Engineering platform for document ingestion, grounded
          retrieval, provider routing, evaluation gates and observable LLM
          operations.
        </p>

        <div className="hero-actions" aria-label="Project links">
          <a href="/demo">Demo placeholder</a>
          <a href="/evidence">Evidence placeholder</a>
        </div>
      </section>

      <section className="feature-grid" aria-label="Platform features">
        {platformFeatures.map((feature) => (
          // Go through each feature in the list and generate HTML from it.
          // `key` helps React with rendering
          <article key={feature} className="feature-card">
            <h2>{feature}</h2>
            <p>
              Planned as part of the platform roadmap and implemented across
              focused milestones.
            </p>
          </article>
        ))}
      </section>
    </main>
  );
}
