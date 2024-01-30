export default function MovieNominationsRow({ movie, i, watched, setWatched }) {
  return (
    <tr>
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
        <input
          type="checkbox"
          id="cbox1"
          checked={watched[movie[0]] ?? false}
          onChange={(e) => {
            let newWatched = { ...watched };
            newWatched[movie[0]] = !watched[movie[0]];
            if (!newWatched[movie[0]]) {
              delete newWatched[movie[0]];
            }
            localStorage.setItem("watched", JSON.stringify(newWatched));
            setWatched(newWatched);
          }}
        />
      </th>
    </tr>
  );
}
