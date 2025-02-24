// Importar o módulo MongoClient
const {MongoClient} = require('mongodb');

// Função principal
async function main() {
    // Definir a URI de conexão com o MongoDB
    const uri = "mongodb://localhost:27017";
    // Criar instância do cliente mongo
    const client = new MongoClient(uri);

    try{
        // Conecta com o servidor MongoDB
        await client.connect();
        // Seleciona o banco de dados "biblioteca"
        const database = client.db('biblioteca-aula');
        // Selecionar a coleção "livros"
        const livros = database.collection('livros');
        //Inserindo informações no banco
        await livros.insertMany([
            {titulo:"1984", autor:"Geoge Owen", ano:1949, genero:"Distopia"},
            {titulo:"Dom Casmurro", autor:"Machado de Assis", ano:1899, genero:"Romance"},
            {titulo:"Senhor dos Aneis", autor:"J.R.R. Tolkei", ano:1954, genero:"Fantasia"},
        ]);
    }finally{
        await client.close();
    }
}
// Chama a função principal e captura o erro, se houver
main().catch(console.error);