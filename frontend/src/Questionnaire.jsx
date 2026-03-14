import { useState } from "react";

function Questionnaire() {
  const [trustSize, setTrustSize] = useState(2000000);
  const [jurisdiction, setJurisdiction] = useState("South Dakota");
  const [needsDirectedTrust, setNeedsDirectedTrust] = useState(true);
  const [needsExternalAdvisor, setNeedsExternalAdvisor] = useState(true);
  const [result, setResult] = useState(null);

  const submitForm = async () => {
    const response = await fetch("http://127.0.0.1:8000/match", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        trust_size: Number(trustSize),
        jurisdiction: jurisdiction,
        needs_directed_trust: needsDirectedTrust,
        needs_external_advisor: needsExternalAdvisor,
      }),
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <section>
      <h2>Trustee Matching</h2>

      <div style={{ marginBottom: "12px" }}>
        <label>Trust Size</label>
        <br />
        <input
          type="number"
          value={trustSize}
          onChange={(e) => setTrustSize(e.target.value)}
        />
      </div>

      <div style={{ marginBottom: "12px" }}>
        <label>Jurisdiction</label>
        <br />
        <input
          type="text"
          value={jurisdiction}
          onChange={(e) => setJurisdiction(e.target.value)}
        />
      </div>

      <div style={{ marginBottom: "12px" }}>
        <label>
          <input
            type="checkbox"
            checked={needsDirectedTrust}
            onChange={(e) => setNeedsDirectedTrust(e.target.checked)}
          />
          Needs Directed Trust
        </label>
      </div>

      <div style={{ marginBottom: "12px" }}>
        <label>
          <input
            type="checkbox"
            checked={needsExternalAdvisor}
            onChange={(e) => setNeedsExternalAdvisor(e.target.checked)}
          />
          Needs External Advisor
        </label>
      </div>

      <button onClick={submitForm}>Find Trustees</button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Top Trustee Matches</h3>
          {result.map((trustee, index) => (
            <div
              key={index}
              style={{
                border: "1px solid #ccc",
                borderRadius: "8px",
                padding: "12px",
                marginBottom: "12px",
                maxWidth: "500px"
              }}
            >
              <strong>{trustee.trustee_name}</strong>
              <div>Score: {trustee.score}</div>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}

export default Questionnaire;