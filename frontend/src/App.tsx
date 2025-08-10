import React from 'react'
import { useEffect, useState } from 'react'
import { getHealth } from './api'

function App() {
  const [status, setStatus] = useState<string>('checking...')
  useEffect(() => {
    getHealth().then(r => setStatus(r.status)).catch(() => setStatus('unreachable'))
  }, [])

  return (
    <div style={{ padding: 24, fontFamily: 'system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, sans-serif' }}>
      <h1>AL Saad Analytics</h1>
      <p>Backend health: {status}</p>
    </div>
  )
}

export default App


