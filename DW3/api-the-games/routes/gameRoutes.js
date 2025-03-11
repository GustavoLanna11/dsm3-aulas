import express from "express";
const gameRoutes = express.Router();
import gameController from "../controllers/gameController.js";

//Sem problemas a rota ser a mesma, pq o método é quem vai deixar tudo ok

// Endpoint para listar todos os games (rota)
gameRoutes.get("/games", gameController.getAllGames);

//Endpoint para cadastrar um jogo
gameRoutes.post("/games", gameController.createGame);

//Endpoint para excluir um jogo
gameRoutes.delete("/games/:id", gameController.deleteGame);

export default gameRoutes;
