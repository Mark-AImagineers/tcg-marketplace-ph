import React from 'react';

export default function CardForm({ formData, onChange }) {
  return (
    <div className="panel left">
      <h2>Card Detail Form</h2>
      <input name="name" placeholder="Name" value={formData.name} onChange={onChange} />
      <input name="set_num" placeholder="Set #" value={formData.set_num} onChange={onChange} />
      <input name="hp" placeholder="HP" value={formData.hp} onChange={onChange} />
      <input name="types" placeholder="Type(s)" value={formData.types} onChange={onChange} />
      <input name="attacks" placeholder="Attacks" value={formData.attacks} onChange={onChange} />
    </div>
  );
}
