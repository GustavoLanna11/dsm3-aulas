import mongoose from "mongoose";

//Documento aninhado - geralmente o aninhado é criado primeiro, pois no documento principal, será referenciado o documento recebido.
const descriptionSchema = new mongoose.Schema({
  genre: String,
  platform: String,
  rating: String
})

const gameSchema = new mongoose.Schema({
  title: String,
  //Pelo plataforma já estar acima, não é necessário aqui! platform: String,
  year: Number,
  price: Number,
  //incluindo documento aninhado
  descriptions: [descriptionSchema] //Array de objetos 
});

// Aqui está sendo criado a coleção games no banco de dados
const Game = mongoose.model("Game", gameSchema);

export default Game;
