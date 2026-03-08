/**
 * Root frontend component for the TrustOS MVP.
 *
 * This file will eventually coordinate app-level state and routing
 * between the questionnaire and results views.
 */

import Questionnaire from "./Questionnaire";
import Results from "./Results";

function App() {
  return (
    <main>
      <h1>TrustOS MVP</h1>
      {/* Placeholder composition until app state is implemented */}
      <Questionnaire />
      <Results />
    </main>
  );
}

export default App;
