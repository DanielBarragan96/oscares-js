import { useState } from "react";

function Category({ title, nominees }) {
  let [selectedOption, setSelectedOption] = useState(
    localStorage.getItem(title) ?? ""
  );

  function handleOptionChange(changeEvent) {
    let selection = changeEvent.target.value;
    setSelectedOption(selection);
    localStorage.setItem(title, selection);
  }
  return (
    <div className="Category">
      <h3>{title}</h3>
      {nominees.map((nominee, i) => (
        <div key={i} className="nominee">
          <label>
            <input
              type="radio"
              value={nominee}
              checked={selectedOption === nominee}
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
