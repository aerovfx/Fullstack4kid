import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Box } from '@mui/material';

import { Navbar } from './components';
import { Feed } from "@mui/icons-material";

function App() {
  return (
    <BrowserRouter>
      <Box sx={{ backgroundColor: '#0000' }}>
        <Navbar />
        <Feed />
        
      </Box>
    </BrowserRouter>
  );
}

export default App;
