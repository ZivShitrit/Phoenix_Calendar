//npm run dev

import { useEffect, useState } from 'react';

function App() {
  const [calendarData, setCalendarData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/calendar')
      .then((res) => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then((data) => {
        setCalendarData(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Fetch error:', err);
        setLoading(false);
      });
  }, []);

  return (
    <div>
      <h1>Calendar Data</h1>
      {loading ? (
        <p>Loading...</p>
      ) : calendarData ? (
        <pre>{JSON.stringify(calendarData, null, 2)}</pre>
      ) : (
        <p>Failed to load data.</p>
      )}
    </div>
  );
}

export default App;

