import {Navbar,Container,Nav} from 'react-bootstrap';
import ss_logo from '../assets/Images/ss_logo.jpeg';
import navIcon1 from '../assets/Images/nav-icon1.svg';
import navIcon2 from '../assets/Images/nav-icon2.svg';
import navIcon3 from '../assets/Images/nav-icon3.svg';
import { useEffect,useState } from 'react';
// import { HashLink } from 'react-router-hash-link';

const NavBar = () => {
    const [isLinkActive,setIsLinkActive] = useState('home');
    const [scrolled,setScrolled] = useState(false);
    useEffect(() => {
      const onScroll = () => {
        if (window.scrollY > 50) {
          setScrolled(true);
        } else {
          setScrolled(false);
        }
      }
  
      window.addEventListener("scroll", onScroll);
  
      return () => window.removeEventListener("scroll", onScroll);
    }, [])
  
    const onUpdateActiveLink = (value) => {
      setIsLinkActive(value);
    }

    return (
    <>
     <Navbar expand="md">
        <Container>
          <Navbar.Brand href="/">
            {/* <img src={ss_logo} alt="Logo" /> */}
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav">
            <span className="navbar-toggler-icon"></span>
          </Navbar.Toggle>
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="ms-auto">
              <Nav.Link href="#home" className={isLinkActive === 'home' ? 'active navbar-link' : 'navbar-link'} onClick={() => onUpdateActiveLink('home')}>Home</Nav.Link>
              <Nav.Link href="#skills" className={isLinkActive === 'skills' ? 'active navbar-link' : 'navbar-link'} onClick={() => onUpdateActiveLink('skills')}>Skills</Nav.Link>
              <Nav.Link href="#projects" className={isLinkActive === 'projects' ? 'active navbar-link' : 'navbar-link'} onClick={() => onUpdateActiveLink('projects')}>Projects</Nav.Link>
            </Nav>
            <span className="navbar-text">
              <div className="social-icon">
                <a href="#"><img src={navIcon1} alt="" /></a>
                <a href="#"><img src={navIcon2} alt="" /></a>
                <a href="#"><img src={navIcon3} alt="" /></a>
              </div>
              {/* <HashLink to='#connect'> */}
                <button className="vvd"><span>Let’s Connect</span></button>
              {/* </HashLink> */} 
            </span>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
    );
};

export default NavBar;