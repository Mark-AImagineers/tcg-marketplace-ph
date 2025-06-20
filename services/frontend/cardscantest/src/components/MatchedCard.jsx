import React from 'react';

export default function MatchedCard({ card }) {
  if (!card) {
    return (
      <div className="panel center">
        <h2>Matched Card Info</h2>
        <p>No card matched yet.</p>
      </div>
    );
  }

  return (
    <div className="panel center">
      <h2>Matched Card Info</h2>
      <p><strong>Name:</strong> {card.name}</p>
      <p><strong>Set #:</strong> {card.set_num}</p>
      <p><strong>Rarity:</strong> {card.rarity}</p>
      <p><strong>Evolves From:</strong> {card.evolves_from}</p>
    </div>
  );
}
