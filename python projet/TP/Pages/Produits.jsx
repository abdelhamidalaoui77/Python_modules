import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './Page.css'; 
import Supprimer from './CRUD/Supprimer'
import Modifier from './CRUD/Modifier';

function Produits() {
    const [produits, setProduits] = useState([]);

    const getProduites = () => {
        fetch("http://localhost:8000/produites")
            .then((response) => response.json())
            .then((response) => setProduits(response))
            .catch((err) => console.error("Error fetching data:", err));
    };

    const List = produits.map((produit) => {
        return (
            <tr key={produit.id}>
                <td>{produit.id}</td>
                <td>{produit.nom}</td>
                <td>{produit.prix} DH</td>
                <td>{produit.enstock === true ? <img src="/assets/happy.png" width={"35px"} alt='happy face'/> : <img src="/assets/angry.png" width={"35px"} alt='angry face'/>}</td>
                <td>
                    {/* Update the link to use id */}
                    <Link to={`/produites/${produit.id}`} className="details-link">
                        ➔
                    </Link>
                </td>
                <td> <Modifier produit={produits}/> </td>
                <td> <Supprimer id={produit.id} fetchProduites={getProduites}/> </td>
            </tr>
        );
    });

    useEffect(() => {
        getProduites();
    }, []);

    return (
        <>
            <h1 className="text-center mt-4 mb-5">Liste des produits</h1>
            <div className="table-container">
                <table className="table table-bordered table-hover custom-table">
                    <thead>
                        <tr>
                            <th scope="col">Ref</th>
                            <th scope="col">Nom</th>
                            <th scope="col">Prix</th>
                            <th scope="col">En stock</th>
                            <th scope="col">Plus de détails</th>
                            <th scope="col" colSpan={2}>action</th>
                        </tr>
                    </thead>
                    <tbody>{List}</tbody>
                </table>
            </div>
        </>
    );
}

export default Produits;
