import React from 'react';

export default function SQLPreview({ query }) {
  return (
    <div className="panel right">
      <h2>SQL Preview</h2>
      <pre>{query}</pre>
    </div>
  );
}
