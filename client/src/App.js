import logo from './logo.svg';
import {Router,Routes,Route} from 'react-router-dom';
import './App.css';
import Registration from './components/Registration';

function App() {
  return (
    <div className="App">
      <Router>
      
      <Routes>
        <Route path='/' element={Registration}/>
      </Routes>
      </Router>
      
      
    </div>
  );
}

export default App;
