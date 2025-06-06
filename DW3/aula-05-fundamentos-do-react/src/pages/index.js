import Counter from "@/components/Counter";
import Descriptions from "@/components/Descriptions";
import Dog from "@/components/Dog";
import Form from "@/components/Form";
import Parent from "@/components/Parent";
import TrafficLight from "@/components/TrafficLight";
import User from "@/components/User";
import Welcome from "@/components/Welcome";
import Head from "next/head";
import TaskList from "@/components/TaskList";

export default function Home() {
  return (
    <>
      <Head>
        <title>Fundamentos do React</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <h1>Hello world!</h1>
        {/* Comentário em JSX */}
        {/* Chamando o componente */}
        <Welcome />
        {/* Importando o componente User que possui uma expressão JSX */}
        <User />
        {/* Componente pai que possui um compnente filho incorporado */}
        <Parent />
        {/* Chamando o componente e passando as props para o mesmo: */}
        <Descriptions name="Diego" age={18} />
        {/* Usando a desestruturação para passar props */}
        <Dog name="Rex" breed="Pitbull" />
        <br />
        {/* Contador */}
        <Counter />
        <br /><br />
        {/* Semáforo (estados) */}
        <TrafficLight />
        <br /><br />
        {/* Formulário de cadastro */}
        <Form />
        <br />
        <br />
        {/* Passando a lista de tarefas por PROPS */}
        <TaskList tasks={[
          {
            id: 1,
            text: "Estudar React"
          },
          {
            id: 2,
            text: "Pagar os Boletos"
          },
          {
            id: 3,
            text: "Retirar o Lixo"
          },
          {
            id: 4,
            text: "Lavar Roupa"
          },

          ]}/>
        <br />
        <br />
        <br />
      </main>
    </>
  );
}
