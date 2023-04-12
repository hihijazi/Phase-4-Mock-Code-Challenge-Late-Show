import { useEffect, useState } from "react";

function GuestForm({ episodeId, onAddGuest }) {
  const [guests, setGuests] = useState([]);
  const [guestId, setGuestId] = useState("");
  const [rating, setRating] = useState("");
  const [formErrors, setFormErrors] = useState([]);

  useEffect(() => {
    fetch("/guests")
      .then((r) => r.json())
      .then(setGuests);
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    const formData = {
      guest_id: guestId,
      episode_id: episodeId,
      rating: parseInt(rating),
    };
    fetch("/appearances", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    }).then((r) => {
      if (r.ok) {
        r.json().then((appearance) => {
          onAddGuest(appearance.guest);
          setFormErrors([]);
        });
      } else {
        r.json().then((err) => setFormErrors(err.errors));
      }
    });
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="guest_id">Guest:</label>
      <select
        id="guest_id"
        name="guest_id"
        value={guestId}
        onChange={(e) => setGuestId(e.target.value)}
      >
        <option value="">Select a Guest</option>
        {guests.map((guest) => (
          <option key={guest.id} value={guest.id}>
            {guest.name}
          </option>
        ))}
      </select>
      <label htmlFor="rating">Rating:</label>
      <input
        id="rating"
        name="rating"
        type="number"
        value={rating}
        onChange={(e) => setRating(e.target.value)}
      />
      {formErrors.length > 0
        ? formErrors.map((err) => (
            <p key={err} style={{ color: "red" }}>
              {err}
            </p>
          ))
        : null}
      <button type="submit">Add To Episode</button>
    </form>
  );
}

export default GuestForm;
