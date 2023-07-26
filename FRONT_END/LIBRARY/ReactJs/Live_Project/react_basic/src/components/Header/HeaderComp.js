import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

const Header = () => {
  return (
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
        <Navbar.Brand href="#home">May's store</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#Users">users</Nav.Link>
            <Nav.Link href="#Admins">admins</Nav.Link>
            
          </Nav>
          <Nav>
            <NavDropdown title="Setting" id="basic-nav-dropdown">
                
                <NavDropdown.Item href="#login">
                  Log in
                </NavDropdown.Item>
                <NavDropdown.Item href="#logout">Log out</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#profile">
                  Profile
                </NavDropdown.Item>
              </NavDropdown>

          </Nav>

        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Header;