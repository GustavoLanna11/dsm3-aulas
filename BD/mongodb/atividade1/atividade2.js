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
        const navesTripulantes = database.collection('navesTripulantes');

        /*//2 - inserindo as informações no nosso banco
        await naves.insertMany([
            {nome: "Estrela Cadente", tipo: "Exploração", capacidadetripulantes: 20, emMissao: true },
            {nome: "Colossus", tipo: "Carga", capacidadetripulantes: 40, emMissao: false },
            {nome: "Anakin", tipo: "Combate", capacidadetripulantes: 5, emMissao: true },
            {nome: "Skywalker", tipo: "Combate", capacidadetripulantes: 2, emMissao: true },
        ])*/

        //3 - Consultando naves que estão em missão
        const navesMissao = await naves.find({emMissao:true}).toArray();
        console.log('Naves em missão: ', navesMissao);

        /*// 3 - naves com capacidade maior que 5 tripulantes
        const navesTripulantes = await naves.find({capacidadetripulantes: {$gt:5}}).toArray();
        console.log('Naves com mais de 5 tripulantes: ', navesTripulantes);*/

        /*// 4 - Atualizando as naves de frota para não estar em missão
        await naves.updateMany(
            {tipo: "Carga" }, //Filtro para encontrar animais
            {$set: {emMissao:false}} //Valor atualizado para o campo em específico
        );*/

        //Consultando itens pós alteração
        const updatedNaves = await naves.find().toArray();
        console.log('Naves Atualizadas: ', updatedNaves);

        /*//5 - Descomissionamento, naves com capacidade de tripulação < 3 serão excluídas
        await naves.deleteMany({ capacidadetripulantes: { $lte: 3}});*/

        //6 - adicionando uma coleção de tripulantes associando as naves 
        await navesTripulantes.insertMany([
            {nome: "Gustavo", funcao: "Guerreiro", patente: "Capitão", naveId: naveAnakin._id},
            {nome: "Isabele", funcao: "Suporte", patente: "Sub-comandante", naveId: naveEstrelaCadente._id},
            {nome: "Chamas", funcao: "Explorador", patente: "Capitão", naveId: naveEstrelaCadente._id},
            {nome: "Isa", funcao: "Asssassina", patente: "Elite", naveId: naveSkywalker._id},
        ])

    } finally{
        await client.close();
    }
}

// Chama a função principal e captura o erro, se houver
main().catch(console.error);