let selectedOption = "";

function handleOptionChange(changeEvent) {
  selectedOption = changeEvent.target.value;
  console.log(selectedOption);
}

function Category({ title, nominees }) {
  return (
    <div className="Category">
      <h1>{title}</h1>
      {nominees.map((nominee, i) => (
        <div key={i}>
          <label>
            <input
              type="radio"
              value={nominee}
              checked={false}
              onChange={handleOptionChange}
            />
            {nominee}
          </label>
        </div>
      ))}
    </div>
  );
}

export default Category;
