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
        const database = client.db('rpg_db');
        //selecionando a coleção personagens
        const personagens = database.collection('personagens');

        //2 - inserindo as informações no nosso banco
        await personagens.insertMany([
            {nome: "Ayra Ventis", classe: "Mago", nivel: 20, hablidades: ["Soco Trovão", "Invisibilidade"], vida: 100 },
            {nome: "Gustavo", classe: "Guerreiro", nivel: 14, hablidades: ["Kiraishiki", "Rapidez Instântanea"], vida: 100 },
            {nome: "Lanna", classe: "Atirador", nivel: 11, hablidades: ["Chuva de Balas", "Perfurador"], vida: 100 },
            {nome: "Isabele", classe: "Suporte", nivel: 20, hablidades: ["Cura Extrema", "Escudo Protetor"], vida: 100 },
            {nome: "Isa", classe: "Atirador", nivel: 20, hablidades: ["Tiro ao Alvo", "1000 tiros"], vida: 100 },
            {nome: "Chamas", classe: "Médico", nivel: 20, hablidades: ["Curador de Primeira", "Vida a mais"], vida: 100 },
            
        ])

        //3 - Consultando personagens maiores que nível 10
        const personagens10 = await personagens.find({nivel: {$gt: 10}}).toArray();
        console.log('Personagens com nível maior que 10: ', personagens10);

        /*// 3 - Encontrando guerreiros
        const guerreiros = await personagens.find({classe: "Guerreiro"}).toArray();
        console.log('Aqui estão os guerreiros: ', guerreiros);*/

        // 4 - Atualizando os guerreiros par 200 de vida
        await personagens.updateMany(
            {classe: "Guerreiro" }, //Filtro para encontrar animais
            {$set: {vida:200}} //Valor atualizado para o campo em específico
        );

        //Consultando itens pós alteração
        const updatedPersonagens = await personagens.find().toArray();
        console.log('Guerreiros atualizados: ', updatedPersonagens);

        //5 - Retirando personagens com menos de 30 de vida
        await personagens.deleteMany({ vida: { $lte: 30}});

    } finally{
        await client.close();
    }
}

// Chama a função principal e captura o erro, se houver
main().catch(console.error);