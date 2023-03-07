import "./App.css";
import Category from "./Category";

const nominations = [
  {
    title: "ACTOR IN A LEADING ROLE",
    nominees: [
      "AUSTIN BUTLER, Elvis",
      "COLIN FARRELL, The Banshees of Inisherin",
      "BRENDAN FRASER, The Whale",
      "PAUL MESCAL, Aftersun",
      "BILL NIGHY, Living",
    ],
  },
];

function App() {
  return (
    <div className="App">
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
