<?php


require('./Toner.php');
require('./Formater.php');
require('./Printer.php');
$response = file_get_contents("data.json");
$decodedArr = json_decode($response, JSON_PRETTY_PRINT);
$printersArr = $decodedArr["printers"];

$printersList = [];
foreach ($printersArr as $i => $printerArr) {
	$printer = new Printer($printerArr);
	$printersList[] = $printer;
}

?>

<!doctype html>
<html lang="en">

<head>
	<title>Drukarki</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link href="css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
	<link href='css/roboto.css' rel='stylesheet' type='text/css'>
	<link rel="stylesheet" href="css/font-awesome.min.css">
	<script src="js/sortable.js"></script>

	<link rel="stylesheet" href="css/style.css">

</head>

<body>
	<section class="ftco-section">
		<div class="container">
			<div class="row justify-content-center">
				<div class="col-md-8 text-center mb-5">
					<h2 class="heading-section">Drukarki</h2>
				</div>
			</div>
			<div class="row">
				<div class="col-md-12">
					<div class="table-wrap table-responsive-xl">
						<table class="table table-hover sortable">
							<thead>
								<tr>

									<th scope="col">#</th>
									<th scope="col">Nazwa</th>
									<th scope="col">Model</th>
									<!--<th scope="col">IP</th>-->

									<th scope="col">Black</th>
									<th scope="col">Cyan</th>
									<th scope="col">Magenta</th>
									<th scope="col">Yellow</th>

									<th scope="col">Ilość str.</th>
									<th scope="col">kolor str.</th>
									<th scope="col">black str.</th>
								</tr>
							</thead>
							<tbody>
								<?php
								foreach ($printersList as $i => $printer) {
									$CyanToner = $printer->CToner;
									$MagentaToner = $printer->MToner;
									$YellowToner = $printer->YToner;
									$BlackToner = $printer->KToner;
								?>

									<tr class="alert" role="alert">
										<!--ID-->
										<td>
											<span><?= $printer->id; ?></span>
										</td>

										<!--NAZWA-->
										<td>
											<span><?= $printer->name; ?></span>


										</td>

										<td><?= $printer->model; ?></td>
										<td class="status"><span class="<?= $BlackToner->cssStyle ?>"><?= $BlackToner->quantity; ?></span></td>
										<td class="status"><span id="colorID" class="<?= $CyanToner->cssStyle ?>"><?= $CyanToner->quantity; ?></span></td>
										<td class="status"><span class="<?= $MagentaToner->cssStyle ?>"><?= $MagentaToner->quantity; ?></span></td>
										<td class="status"><span class="<?= $YellowToner->cssStyle ?>"><?= $YellowToner->quantity; ?></span></td>

										<td class="pageNum"><?= $printer->AllPages; ?></td>
										<td class="pageNum"><?= $printer->PagesColor; ?></td>
										<td class="pageNum"><?= $printer->PagesBW; ?></td>
									</tr>
								<?php    } ?>
							</tbody>
						</table>
					</div>
				</div>
			</div>
		</div>
		</div>
	</section>

	<div>
		<?php
		date_default_timezone_set('Europe/Warsaw');
		echo "Last modified: " . date(
			"F d Y H:i:s.",
			filemtime("data.json")
		);
		?>
	</div>

	<script>
		function formatNumber(num) {
			return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
		}

		var y = document.getElementsByClassName("pageNum");
		for (let i = 0; i < y.length; i++) {
			var numb = y[i].innerHTML;
			
			y[i].innerHTML = formatNumber(numb);

			if(numb==0)
			{
				y[i].innerHTML=" ";
			}
		}
	</script>

	<script src="js/jquery.min.js"></script>
	<script src="js/popper.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/main.js"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>

</body>

</html>