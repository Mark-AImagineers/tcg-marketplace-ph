import React from 'react';

export default function TopBar({ onMatch }) {
  return (
    <div className="top-bar">
      <button disabled>📸 Capture Card</button>
      <button disabled>📁 Upload Image</button>
      <button onClick={onMatch}>🔁 Match Now</button>
    </div>
  );
}
