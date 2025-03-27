// Importando o módulo do mongoClient
const {MongoClient} = require('mongodb');

//Criação da função principal
async function main(){
    //Definindo a conexão com o mongo
    const uri = "mongodb://127.0.0.1:27017";
    //criando instância do cliente
    const client = new MongoClient(uri);

    try {
        //Conectando com o servidor 
        await client.connect();
        //1 - selecionando o banco
        const database = client.db('space_db');
        //selecionando a coleção naves
        const naves = database.collection('naves');
        //selecionando tripulantes
        const tripulantes = database.collection('tripulantes');

        //2 - inserindo as informações no nosso banco
       const navesInseridas =  await naves.insertMany([
            {nome: "Estrela Cadente", tipo: "Exploração", capacidadetripulantes: 20, emMissao: true },
            {nome: "Colossus", tipo: "Carga", capacidadetripulantes: 40, emMissao: false },
            {nome: "Anakin", tipo: "Combate", capacidadetripulantes: 5, emMissao: true },
            {nome: "Skywalker", tipo: "Combate", capacidadetripulantes: 2, emMissao: true },
        ])

        const idNaves = navesInseridas.insertedIds;

        //3 - Consultando naves que estão em missão
        const navesMissao = await naves.find({emMissao:true}).toArray();
        console.log('Naves em missão: ', navesMissao);

        // 3 - naves com capacidade maior que 5 tripulantes
        const navesTripulantes = await naves.find({capacidadetripulantes: {$gt:5}}).toArray();
        console.log('Naves com mais de 5 tripulantes: ', navesTripulantes);

        // 4 - Atualizando as naves de frota para não estar em missão
        await naves.updateMany(
            {tipo: "Carga" }, //Filtro para encontrar animais
            {$set: {emMissao:false}} //Valor atualizado para o campo em específico
        );

        //Consultando itens pós alteração
        const updatedNaves = await naves.find().toArray();
        console.log('Naves Atualizadas: ', updatedNaves);

        //5 - Descomissionamento, naves com capacidade de tripulação < 3 serão excluídas
        await naves.deleteMany({ capacidadetripulantes: { $lte: 3}});

        //6 - adicionando uma coleção de tripulantes associando as naves 
        await tripulantes.insertMany([
            {nome: "Gustavo", funcao: "Guerreiro", patente: "Capitão", idNave: idNaves['1']},
            {nome: "Isabele", funcao: "Suporte", patente: "Sub-comandante", idNave: idNaves['2']},
            {nome: "Chamas", funcao: "Explorador", patente: "Capitão", idNave: idNaves['3']},
            {nome: "Isa", funcao: "Asssassina", patente: "Elite", idNave: idNaves['1']},
        ])

         console.log("Tripulantes inseridos com sucesso.");

    } finally{
        await client.close();
    }
}

// Chama a função principal e captura o erro, se houver
main().catch(console.error);