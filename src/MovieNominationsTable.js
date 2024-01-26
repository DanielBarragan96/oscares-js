function MovieNominationsTable({ movieNominations }) {
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
              <th>
                <input type="checkbox" id="cbox1" value="first_checkbox" />
              </th>
            </tr>
          ))}
        </tbody>
      </table>
      <h1>Total watched: {0}</h1>
      <h5> </h5>
    </>
  );
}

export default MovieNominationsTable;
