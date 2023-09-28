import { Controller } from "@hotwired/stimulus";
import Alert from 'bootstrap/js/dist/alert';

export default class extends Controller {
    connect() {
        const alert = new Alert(this.element);
        setTimeout(() => alert.close(), 2500);
    }
}