import React from 'react';

const DebugInfo = () => {
  // Only show debug info in development
  if (process.env.NODE_ENV === 'production') {
    return null;
  }

  return (
    <div style={{ 
      position: 'fixed', 
      bottom: 0, 
      right: 0, 
      background: 'rgba(0,0,0,0.8)', 
      color: 'white', 
      padding: '10px', 
      fontSize: '12px',
      zIndex: 10000
    }}>
      <div>API Base URL: {process.env.REACT_APP_API_URL || 'Not set'}</div>
      <div>NODE_ENV: {process.env.NODE_ENV}</div>
    </div>
  );
};

export default DebugInfo;