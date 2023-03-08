import "./App.css";
import Category from "./Category";
import oscar from "./oscar.png";

import nominations from "./nominations.json";

function App() {
  return (
    <div className="App">
      <img src={oscar} alt="oscar" />
      <h1>95th Academy Awards</h1>
      {nominations.map((nomination, i) => (
        <Category
          title={nomination.title}
          nominees={nomination.nominees}
          key={i}
        />
      ))}
    </div>
  );
}

export default App;
