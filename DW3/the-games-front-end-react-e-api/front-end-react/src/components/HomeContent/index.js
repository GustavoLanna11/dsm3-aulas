import styles from "@/components/HomeContent/HomeContent.module.css";
import Loading from "../Loading";
import axios from "axios";
import { useState, useEffect } from "react";

const HomeContent = () => {
//Criando um estado para games
const [games, setGames] = useState([]);



  // efeito colateral
useEffect(() =>{
  const fetchGames = async () =>{
    try{
      const response = await axios.get("http://localhost:4000/games")
      // console.log(response)
      //Pegando uma lista de games e colando no estado
      setGames(response.data.games)
    }catch(error) {
      console.log(error)
    }
  };
  //invocando a função
  fetchGames();
}, []); //Depêndencia do useEffect


//função para deletar
const deleteGame = async (gameId) => {
  try{
    const response = await axios.delete(
      `http://localhost:4000/games/${gameId}`
    );
    if (response.status === 204) {
      alert("Jogo excluído com sucesso")
    }
  }
};

  return (
    <>
      <div className={styles.homeContent}>
        {/* CARD LISTA DE JOGOS */}
        <div className={styles.listGamesCard}>
          {/* TITLE */}
          <div className={styles.title}>
            <h2>Lista de jogos</h2>
          </div>
          {/* <Loading /> */}
          <div className={styles.games} id={styles.games}>

            {/* Lista de jogos irá aqui */}
            {games.map((game) => (
              <ul key={game._id} className={styles.listGames}> 
              <div className={styles.gameImg}>
                <img src="images/game_cd_cover.png" alt="Jogo em estoque" />
              </div>
              <div className={styles.gameInfo}>
                <h3>{game.title}</h3>
                <li>Plataforma: {game.descriptions.platform}</li>
                <li>Gênero: {game.descriptions.genre}</li> 
                <li>Classificação: {game.descriptions.rating}</li> 
                <li>Ano: {game.year}</li>
                <li>Preço: {game.price.toLocaleString("pt-br", {style: "currency", currency: "BRL"})}</li>
                {/* Botão para excluir */}
                <button className={styles.btnDel} onClick={() => {
                  const confirmed = window.confirm("Deseja mesmo excluir o jogo?");
                  if(confirmed) {
                    return;
                  }
                }}>Deletar</button>
              </div>
              </ul>
            ))}
           
          </div>
        </div>
      </div>
    </>
  );
};

export default HomeContent;
