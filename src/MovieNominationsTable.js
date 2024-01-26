function MovieNominationsTable({ movieNominations }) {
  return (
    <table>
      <tbody>
        <tr>
          <th></th>
          <th>
            <h3>Movie</h3>
          </th>
          <th>
            <h3>Total Nominations</h3>
          </th>
        </tr>
        {movieNominations.map((movie, i) => (
          <tr key={movie}>
            <th>
              <label>{i + 1}</label>
            </th>
            <th>
              <label>{movie[0]}</label>
            </th>
            <th>
              <label>{movie[1]}</label>
            </th>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default MovieNominationsTable;
