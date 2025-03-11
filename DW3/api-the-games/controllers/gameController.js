import gameService from "../services/gameService.js";
import {ObjectId} from 'mongodb';

const getAllGames = async (req, res) => {
  try {
    const games = await gameService.getAll();
    // Requisição feita com sucesso - Cod. 200 (OK)
    res.status(200).json({ games: games });
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: "Erro interno do servidor." });
  }
};

//Função para cadastrar Jogos
const createGame = async (req, res) => {
  try {
    //Desestruturação
    const { title, platform, year, price } = req.body;
    await gameService.Create(title, platform, year, price);
    res.sendStatus(201);
  } 
  catch (error) {
    console.log(error);
    res.status(500).json({ error: "Erro interno do servidor" });
  }
};

//Função para deletar jogos
const deleteGame = async  (req,res) => {
  try{
    if(ObjectId.isValid(req.params.id)) {
      const {id} = req.params
      gameService.Delete(id);
      res.sendStatus(204) // No content
    } else {
      res.sendStatus(400) // Código 400 (bad request)
    }
  } catch{
    console.log(error)
    res.status(500).json({ error: "Erro interno do servidor"})
  }
}

export default { getAllGames, createGame, deleteGame };
