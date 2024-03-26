<script lang="ts">
  import { writable } from 'svelte/store';
  import { superForm, SuperValidated, Infer } from "sveltekit-superforms";
  import { zodClient } from "sveltekit-superforms/adapters";
  import { formSchema, FormSchema } from "./schema";
  import * as Form from "./index";

  interface FormData {
    subproperty_type: string;
    region: string;
    province: string;
    locality: string;
    zip_code: number;
    total_area_sqm: number;
    surface_land_sqm: number;
    nbr_frontages: number;
    nbr_bedrooms: number;
    equipped_kitchen: string;
    fl_furnished: number;
    fl_open_fire: number;
    fl_terrace: number;
    terrace_sqm: number;
    fl_garden: number;
    garden_sqm: number;
    fl_swimming_pool: number;
    fl_floodzone: number;
    state_building: string;
    primary_energy_consumption_sqm: number;
    epc: number;
    heating_type: string;
    fl_double_glazing: number;
    cadastral_income: number;
  }

  let formDataStore = writable<FormData>({
    subproperty_type: "HOUSE",
    region: "Flanders",
    province: "Antwerp",
    locality: "Antwerp",
    zip_code: 2050,
    total_area_sqm: 200.0,
    surface_land_sqm: 100.0,
    nbr_frontages: 2,
    nbr_bedrooms: 3,
    equipped_kitchen: "INSTALLED",
    fl_furnished: 0,
    fl_open_fire: 0,
    fl_terrace: 1,
    terrace_sqm: 20.0,
    fl_garden: 1,
    garden_sqm: 50.0,
    fl_swimming_pool: 0,
    fl_floodzone: 0,
    state_building: "NEW",
    primary_energy_consumption_sqm: 100.0,
    epc: 200,
    heating_type: "GAS",
    fl_double_glazing: 1,
    cadastral_income: 2000
  });

  let data: SuperValidated<Infer<FormSchema>> = $formDataStore;

  const form = superForm(data, {
    validators: zodClient(formSchema),
  });

  const { form: formData, enhance } = form;

  async function estimate(event: Event): Promise<void> {
    event.preventDefault();
    let response = await fetch('http://127.0.0.1:5000/predict/house', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    });
    let data = await response.json();
    console.log(data);
  }
</script>

<form method="POST" use:enhance on:submit|preventDefault={estimate}>
  <Form.Field form={form} name="subproperty_type">
    <Form.Control let:attrs>
      <Form.Label>Subproperty Type</Form.Label>
      <Form.Input {...attrs} bind:value={formData.subproperty_type} />
    </Form.Control>
    <Form.FieldErrors />
  </Form.Field>
  <!-- Repeat for other fields -->
  <Form.Button type="submit">Submit</Form.Button>
</form>