<template>



	<table class="table">
		<tr>
			<td colspan="2">
				<h1 class="head">{{ mainHeader }}</h1>
			</td>
		</tr>
		<tr v-for="(task, index) in tasks">
			<td>{{ task.text }}</td>
			<td><button @click="deleteTask(index)"> удалить </button> </td>
		</tr>
		<tr>
			<td><input type="text" v-model.trim="textTask" placeholder="задача"
					@keyup.enter="clickButton('mainButton', textTask)">
			</td>
			<td><button id="mainButton" v-show="textTask != ''" @click="addToArray(),
				clearInput()">Добавить</button>
			</td>
		</tr>
	</table>


</template>

<script>
import axios from 'axios'

export default {
	data() {
		return {
			mainHeader: 'to-do list in docker',
			tasks: [],
			textTask: ''
		}
	},
	methods: {
		//добавляю в массив tasks в переменную textTask (все работает в реактивном режиме)
		addToArray() {
			this.tasks.push({
				text: this.textTask

			})
			axios.post('http://localhost:8088/postTest',
				{
					data: {
						text: this.textTask,
					}
				},
				{
					responseType: 'json',
					headers: {
						'Content-Type': 'application/json'

					}
				}

			)
				.then(response => console.log(response.data))
				.catch(error => console.error(error))

		},
		//очистить поле ввода новой задачи
		clearInput() {
			this.textTask = ''
		},
		//удалить задачу из списка (index - номер задачи, с которой функция будет удалять элемент массива, 1 - кол-во удаленных элементов)
		deleteTask(index) {
			this.tasks.splice(index, 1)
			axios.delete('http://localhost:8088/deleteTest',
				{
					id: index
				}
			)
				.then(response => console.log(response.data))
				.catch(error => console.error(error))
		},
		//валидация при внесении задачи в массив
		clickButton(text) {
			if (text != '') { this.addToArray() }
		}
	}
}
</script>

<style scoped>
h1 {
	color: rgb(49, 166, 63);
	font-weight: lighter;
}

.head {
	text-align: center;
}

.table {
	margin: auto;

}

button {
	width: 100px;
}
</style>
