import { Container } from 'react-bootstrap';
import {  Route,
          Routes,
          BrowserRouter } from 'react-router-dom';

import HomeScreen from './screens/HomeScreen';
import ProductScreen from './screens/ProductScreen'

import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <main className='py-3'>
        <Container>
          <Routes>
            <Route path='/' element={<HomeScreen/>} exact/>
            <Route path='product/:id' element={< ProductScreen />} />
          </Routes>
        </Container>        
      </main>
      <Footer />
    </BrowserRouter>
  );
}

export default App;