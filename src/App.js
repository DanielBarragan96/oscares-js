import "./App.css";
import Category from "./Category";
import oscar from "./oscar.png";

import nominations from "./nominations.json";
import winners from "./winners.json";
import { useState, useEffect } from "react";

import Confetti from "react-confetti";

function App() {
  let width = window.screen.width;
  var [height, setHeigth] = useState(window.screen.height);

  useEffect(() => {
    setHeigth(document.documentElement.scrollHeight);
  }, []);

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

  let goodGuesses = 0;
  try {
    Object.keys(winners).forEach((key) => {
      if (winners[key] === localStorage.getItem(key)) goodGuesses++;
    });
  } catch (Error) {}

  return (
    <div className="App">
      <img src={oscar} alt="oscar" />
      <h1>95th Academy Awards</h1>

      {Object.keys(winners).length > 1 ? (
        <>
          <Confetti width={width} height={height} />
          <label>Congratilations, you guessed:</label>
          <h1>
            {goodGuesses} /{nominations.length}
          </h1>
        </>
      ) : (
        <></>
      )}

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
                    <label
                      id={nomination.title}
                      className={
                        !winners[nomination.title]
                          ? ""
                          : winners[nomination.title] ===
                            localStorage.getItem(nomination.title)
                          ? "goodGuess"
                          : "badGuess"
                      }
                    >
                      {localStorage.getItem(nomination.title)}
                    </label>
                    <label className="winner">
                      {winners[nomination.title] &&
                      winners[nomination.title] !==
                        localStorage.getItem(nomination.title)
                        ? " " + winners[nomination.title]
                        : " "}
                    </label>
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
