import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Home() {
  const [episodes, setEpisodes] = useState([]);

  useEffect(() => {
    fetch("/episodes")
      .then((r) => r.json())
      .then(setEpisodes);
  }, []);

  function handleDelete(id) {
    fetch(`/episodes/${id}`, {
      method: "DELETE",
    }).then((r) => {
      if (r.ok) {
        setEpisodes((episodes) =>
          episodes.filter((episode) => episode.id !== id)
        );
      }
    });
  }

  return (
    <section className="container">
      {episodes.map((episode) => (
        <div key={episode.id} className="card">
          <h2>
            <Link to={`/episodes/${episode.id}`}>
              Episode {episode.number} - {episode.date}
            </Link>
          </h2>
          <button onClick={() => handleDelete(episode.id)}>Delete</button>
        </div>
      ))}
    </section>
  );
}

export default Home;
