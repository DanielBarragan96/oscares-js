import { useState } from "react";
import MovieNominationsRow from "./MovieNominationsRow";

function MovieNominationsTable({ movieNominations }) {
  if (!localStorage.getItem("watched")) {
    localStorage.setItem("watched", JSON.stringify({}));
  }
  var [watched, setWatched] = useState(
    JSON.parse(localStorage.getItem("watched"))
  );
  return (
    <>
      <table>
        <tbody>
          <tr>
            <th>
              <h3>Position</h3>
            </th>
            <th>
              <h3>Movie</h3>
            </th>
            <th>
              <h3>Total Nominations</h3>
            </th>
            <th>
              <h3>Watched</h3>
            </th>
          </tr>
          {movieNominations.map((movie, i) => (
            <MovieNominationsRow
              key={movie}
              movie={movie}
              i={i}
              watched={watched}
              setWatched={setWatched}
            />
          ))}
        </tbody>
      </table>
      <h1>
        Total watched: {Object.keys(watched).length} / {movieNominations.length}
      </h1>
      <h5> </h5>
    </>
  );
}

export default MovieNominationsTable;
