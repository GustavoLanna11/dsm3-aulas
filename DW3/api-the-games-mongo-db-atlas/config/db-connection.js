//importando o mongoose
import mongoose from "mongoose";

//Usuário e senha do banco dados
const dbUser = "gustavolannam";
const dbPassword = "IyTCK49wxJL8zSDN";
const connect = () => {
    mongoose.connect(
        `mongodb+srv://${dbUser}:${dbPassword}@db-gusta.ywex8.mongodb.net/api-thegames?retryWrites=true&w=majority&appName=db-gusta`
    );

    const connection = mongoose.connection;
    connection.on("error", () => {
        console.log("Erro ao conectar com o mongoDB");
    });
    connection.on("open", () => {
        console.log("Conectando ao mongoDB com sucesso!");
    });
};
connect();
export default mongoose;
