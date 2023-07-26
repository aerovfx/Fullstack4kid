// import logo from './logo.svg';
import './App.css';
import Header from './components/Header/HeaderComp';
// import MyComponent from './components/MyComponent';
import { Link } from 'react-router-dom';


function App() {
  return (
    <div>
      <Header />
      <div>
        test router
      </div>
      <button>
      <Link to="/users">User Page</Link>  
      
      </button>
      <button>
      <Link to="/admins"> Admin Page</Link> 
      </button>
    
    </div>
  );
}

export default App;
