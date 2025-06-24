import { useState } from 'react';
import './App.css';
import TopBar from './components/TopBar';
import CardForm from './components/CardForm';
import MatchedCard from './components/MatchedCard';
import SQLPreview from './components/SQLPreview';

function App() {
  const [formData, setFormData] = useState({
    name: '',
    set_num: '',
    hp: '',
    types: '',
    attacks: '',
  });

  const [matchedCard, setMatchedCard] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleMatch = () => {
    // placeholder for now
    setMatchedCard({
      name: 'Pikachu V',
      set_num: '045/196',
      rarity: 'Ultra Rare',
      evolves_from: 'Pichu',
    });
  };

  const generateSQL = () => {
    let conditions = [];
    if (formData.name) conditions.push(`name ILIKE '%${formData.name}%'`);
    if (formData.set_num) conditions.push(`set_num = '${formData.set_num}'`);
    if (formData.hp) conditions.push(`hp = '${formData.hp}'`);
    if (formData.types) conditions.push(`types @> '{${formData.types}}'`);
    if (formData.attacks) conditions.push(`attacks @> '{${formData.attacks}}'`);
    return `SELECT * FROM cards${conditions.length ? ' WHERE ' + conditions.join(' AND ') : ''};`;
  };

  return (
    <>
      <TopBar onMatch={handleMatch} />
      <div className="layout">
        <CardForm formData={formData} onChange={handleChange} />
        <MatchedCard card={matchedCard} />
        <SQLPreview query={generateSQL()} />
      </div>
    </>
  );
}

export default App;
