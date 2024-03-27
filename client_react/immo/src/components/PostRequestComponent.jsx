function PostRequestComponent() {
  const [responseData, setResponseData] = useState(null);
  const [showModal, setShowModal] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const url = "http://127.0.0.1:5000/predict/house";

    // Hardcoded data to be sent
    const data = {
      subproperty_type: "HOUSE",
      region: "Flanders",
      province: "Antwerp",
      locality: "Antwerp",
      zip_code: 2050,
      total_area_sqm: 200.0,
      surface_land_sqm: 100.0,
      nbr_frontages: 2,
      nbr_bedrooms: 3,
      equipped_kitchen: "INSTALLED",
      fl_furnished: 0,
      fl_open_fire: 0,
      fl_terrace: 1,
      terrace_sqm: 20.0,
      fl_garden: 1,
      garden_sqm: 50.0,
      fl_swimming_pool: 0,
      fl_floodzone: 0,
      state_building: "NEW",
      primary_energy_consumption_sqm: 100.0,
      epc: 200,
      heating_type: "GAS",
      fl_double_glazing: 1,
      cadastral_income: 2000,
    };

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const responseData = await response.json(); // Rename this variable
      console.log(responseData);
      setResponseData(responseData);
      setShowModal(true);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const handleClose = () => {
    setShowModal(false); // Hide the modal
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <button type="submit">Submit</button>
      </form>
      {showModal && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={handleClose}>
              &times;
            </span>
            <h3>Response:</h3>
            <pre>{JSON.stringify(responseData, null, 2)}</pre>{" "}
            {/* Display the response data */}
          </div>
        </div>
      )}
    </div>
  );
}

export default PostRequestComponent;
