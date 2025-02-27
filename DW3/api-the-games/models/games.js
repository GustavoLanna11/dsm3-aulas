import mongoose from "mongoose";

//criando o esquema da coleção chamada games (entidade)
const gameSchema = new mongoose.Schema({
  title: String,
  plataform: String,
  year: Number,
  price: Number,
});

//Aqui está sendo criado a coleção games no banco de dados
//Aqui está escrito "Game", mas ao criar, vai pro plural, ou seja "games"
const Game = mongoose.model("Game", gameSchema);
export default Game;
