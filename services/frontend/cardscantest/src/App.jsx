import { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    name: '',
    set_num: '',
    hp: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const generateSQL = () => {
    let conditions = [];
    if (formData.name) conditions.push(`name ILIKE '%${formData.name}%'`);
    if (formData.set_num) conditions.push(`set_num = '${formData.set_num}'`);
    if (formData.hp) conditions.push(`hp = '${formData.hp}'`);
    return `SELECT * FROM cards${conditions.length ? ' WHERE ' + conditions.join(' AND ') : ''};`;
  };

  return (
    <>
      {/* Top Bar */}
      <div style={{ padding: '10px', borderBottom: '1px solid #ccc', display: 'flex', gap: '10px' }}>
        <button disabled>📸 Capture</button>
        <button disabled>📁 Upload</button>
        <button>🔁 Match Now</button>
      </div>

      <div className="layout">
        {/* Left: Form */}
        <div className="panel left">
          <h2>Card Form</h2>
          <input name="name" placeholder="Name" value={formData.name} onChange={handleChange} />
          <input name="set_num" placeholder="Set #" value={formData.set_num} onChange={handleChange} />
          <input name="hp" placeholder="HP" value={formData.hp} onChange={handleChange} />
        </div>

        {/* Middle: Matched Card Info (Placeholder) */}
        <div className="panel center">
          <h2>Matched Card Info</h2>
          <p>This will show matched data from backend.</p>
        </div>

        {/* Right: SQL Preview */}
        <div className="panel right">
          <h2>SQL Preview</h2>
          <pre>{generateSQL()}</pre>
        </div>
      </div>
    </>
  );
}

export default App;
