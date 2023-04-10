// This is a simple Navbar component that displays a logo and a search bar.
// It uses Material-UI's Stack component to align the logo and search bar 
//in a row. The Stack component has some custom styles applied to make it
// sticky at the top of the page with a black background and space between
// the logo and search bar.
import { Link } from 'react-router-dom';
import { Stack } from '@mui/material';

import { logo } from '../utils/constants';
import SearchBar  from './SearchBar';

const Navbar = () => {
  return (
    <Stack 
      direction="row" 
      alignItems="center" 
      p={2} 
      sx={{ position: "sticky", background: '#000', top:0, justifyContent: "space-between" }}> 
      <Link to="/" style={{ display: 'flex', alignItems: 'center', }}>
        <img src ={logo} alt="logo" height={45} />
      </Link>
      <SearchBar />
    </Stack>
   
  )
  
}

export default Navbar
