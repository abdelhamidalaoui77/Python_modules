import Accueil from './Accueil';
import Contact from './Contact';
import Produits from './Produits';
import React from 'react';
import '../../../node_modules/bootstrap/dist/css/bootstrap.min.css'
import { RouterProvider ,createBrowserRouter, NavLink, Outlet  } from 'react-router-dom';
import './Page.css'
import ProduitDetails from './ProduitDetails';
import Ajouter from './CRUD/Ajouter';

export default  function NavBar() {

    const router = createBrowserRouter([
        {
           path:'/',
           element: <Liens/>,
           children:[
            {
            path:'/',
            element:<Accueil/>
           },
           {
            path:'/produites',
            element:<Produits/>
           },
           {
            path:'/contact',
            element:<Contact/>
           },
           {
            path:'/produites/:id',
            element: <ProduitDetails/>
           },
           {
            path:'/manage',
            element: <Ajouter/>
           }
            ]
        }]
    )
    
    function Liens(){
        return <>
                <nav className='header'>
                    <NavLink className='navlink' to='/'>Acceuil</NavLink>
                    <NavLink className='navlink' to='/produites'>Produites</NavLink>
                    <NavLink className='navlink' to='/contact' >Contact</NavLink>
                    <NavLink className='navlink' to='/manage' >manage</NavLink>
                </nav>
                <nav className='container text-center p-2 my-2'>
                    <Outlet/>
                </nav>
        </>
    }
    
    return (
        
        <RouterProvider router={router}/>
        
    );
}
