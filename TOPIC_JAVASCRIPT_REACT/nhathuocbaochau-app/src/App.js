import { BrowerRouter, Routes, Route } from 'react-router-dom';
import { Box } from '@mui/material';

import { Navbar } from './components';

function App () {
    return (
    <BrowerRouter>
        <Box sx={{ backgroundColor: '#0000' }}>
            <Navbar />
           
        </Box>
    </BrowerRouter>
    );
}


export default App;