import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Box } from '@mui/material';

import { Navbar } from './components';

function App() {
  return (
    <BrowserRouter>
      <Box sx={{ backgroundColor: '#0000' }}>
        <Navbar />
        
      </Box>
    </BrowserRouter>
  );
}

export default App;
//https://reactrouter.com/en/main/upgrading/v5#upgrade-to-react-router-v6