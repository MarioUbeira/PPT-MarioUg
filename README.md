PPT-MarioUg  
==================  

Repositorio para o proxecto Pedra, Papel, Tesoiras da materia Modelos de Intelixencia Artificial.  

O obxectivo de esta tarefa e crear un axente que se base nos resultados de partidas anteriores para tentar predicir o seguinte movemento do adversario e así maximizar a súa probabilidade de vitoria.  

Contorna de tarefas  
==================  

| **Contorna de tarefas** | **Observable** | **Axentes** | **Determinista** | **Episódico** | **Estático** | **Discreto** | **Coñecido** |  
|:-----------------------:|:--------------:|:-----------:|:----------------:|:-------------:|:------------:|:------------:|:------------:|  
| RPS                    | Parcial        | Multiaxente | Estocástico      | Episódico      | Estático      | Discreto      | Coñecido     |  

**RPS**: Contorno simple, baseado na interacción por turnos entre o modelo e o oponente.

**Parcial**: O axente non ten acceso á seguinte acción do oponente nin á lóxica que rexe as súas accións, pero si pode observar o historial de turnos xogados ata o momento.

**Multiaxente**: Interveñen na tarefa tanto o modelo como o seu oponente.

**Estocástico**: O resultado dunha acción non é completamente predecible, xa que depende tanto das decisións do oponente como de posibles compoñentes de aleatoriedade no contorno.

**Episódico**: Cada partida é independente do resto; o resultado dunha partida non afecta á seguinte, aínda que o modelo pode valerse dos resultados anteriores para trazar a súa estratexia.

**Estático**: O escenario da tarefa non se modifica durante a partida, esta desenvólvese sen cambios dinámicos no entorno.

**Discreto**: A variedade de accións/estados e finita (Pedra, Papel ou Tesoiras).

**Coñecido**: As regras do xogo son coñecidas polos participantes e non se modifican en ningún momento da partida.

Estrutura do axente
==================  

![](./img/estrutura_do_axente.png)