import "./App.css";
import Category from "./Category";
import oscar from "./oscar.png";

import nominations from "./nominations.json";
import { useState } from "react";

function App() {
  let [submitted, setSubmitted] = useState(
    localStorage.getItem("submitted") !== null
  );

  function submitVote() {
    setSubmitted(true);
    let newDate = new Date();
    localStorage.setItem("submitted", newDate);
    window.scrollTo(0, 0);
    window.location.reload(true);
  }

  function unsubmitVote() {
    setSubmitted(false);
    localStorage.removeItem("submitted");
    window.scrollTo(0, 0);
    window.location.reload(true);
  }

  return (
    <div className="App">
      <img src={oscar} alt="oscar" />
      <h1>95th Academy Awards</h1>
      {submitted ? (
        <>
          <table key={submitted}>
            <tbody>
              {nominations.map((nomination, i) => (
                <tr key={i}>
                  <td>
                    <label>{nomination.title}</label>
                  </td>
                  <td>
                    <label>{localStorage.getItem(nomination.title)}</label>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <h4>{localStorage.getItem("submitted")}</h4>
          <button onClick={unsubmitVote}>Unsubmit</button>
        </>
      ) : (
        <div></div>
      )}
      {nominations.map((nomination, i) => (
        <Category
          title={nomination.title}
          nominees={nomination.nominees}
          key={i}
          submitted={submitted}
        />
      ))}
      <button onClick={submitVote} disabled={submitted}>
        Submit
      </button>
      <h5> </h5>
    </div>
  );
}

export default App;
