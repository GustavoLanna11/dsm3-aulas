import express from "express";
const app = express();

//Configuração do express
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

//Rota principal
app.get("/", (req, res) => {
  res.send("API iniciando com sucesso!");
});

//Iniciando o servidor
const port = 4000;
app.listen(port, (error) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`API Rodando em http://localhost:${port}`);
  }
});
