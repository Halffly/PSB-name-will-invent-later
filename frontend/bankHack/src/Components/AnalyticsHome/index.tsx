import { Box, Grid, LinearProgress } from "@material-ui/core";
import React from "react";
import { getAllAppsId } from "../../tools/getAllAppsId";
import Card from "../Card";
import { CardPrototype } from "../Card/Models";

const appsList: CardPrototype[] = [
  {
    id: 0,
    title: "WEB RTC App ПСБ",
    views: 200,
    rate: 4,
    imageUrl:
      "https://cdn.dribbble.com/users/702789/screenshots/15487422/media/b1bdbc126699b7cdad71af724103d51d.png?compress=1&resize=1600x1200",
  },
  {
    id: 0,
    title: "Admin App Кабинет",
    views: 20,
    rate: 4.5,
    imageUrl:
      "https://cdn.dribbble.com/users/1963775/screenshots/15483648/media/8bbf309a418ac6a88f4f755b8b599b04.png?compress=1&resize=1600x1200",
  },
  {
    id: 0,
    title: "ПСБ Кабинет. Виджеты Главный экран",
    views: 200,
    rate: 4,
    imageUrl:
      "https://www.psbank.ru/-/media/Files/Bank/Brand/PSB_logo_original_png.png",
  },
  {
    id: 0,
    title: "ПСБ Кабинет. Виджеты Главный экран",
    views: 200,
    rate: 4,
    imageUrl:
      "https://www.psbank.ru/-/media/Files/Bank/Brand/PSB_logo_original_png.png",
  },
  {
    id: 0,
    title: "ПСБ Кабинет. Виджеты Главный экран",
    views: 200,
    rate: 4,
    imageUrl:
      "https://www.psbank.ru/-/media/Files/Bank/Brand/PSB_logo_original_png.png",
  },
  {
    id: 0,
    title: "Приложение для путешествий",
    views: 200,
    rate: 4,
    imageUrl:
      "https://www.psbank.ru/-/media/Files/Bank/Brand/PSB_logo_original_png.png",
  },
  {
    id: 0,
    title: "ПСБ Кабинет. Виджеты Главный экран",
    views: 200,
    rate: 4,
    imageUrl:
      "https://cdn.dribbble.com/users/653699/screenshots/15489025/media/d7af516032094ebd13ef3fb0f337b95a.png?compress=1&resize=1600x1200",
  },
];

const AnalyticsHome = () => {
  const [data, setData] = React.useState<CardPrototype[]>();
  const [isLoading, setIsLoading] = React.useState(true);

  // eslint-disable-next-line react-hooks/exhaustive-deps
  React.useEffect(() => {
    (async () => {
      const ids = await getAllAppsId();
      if (ids) {
        const arr: CardPrototype[] = [];
        ids.forEach((id, index) => arr.push({ ...appsList[index], id }));
        setData(arr);
        setIsLoading(false);
      }
    })();
  }, []);
  if (isLoading) {
    return <LinearProgress />;
  }
  return (
    <Box marginTop={4}>
      <Grid container spacing={4}>
        {data &&
          data.map((x) => (
            <Grid key={x.id} item md={4} xs={12}>
              <Card {...x} />
            </Grid>
          ))}
      </Grid>
    </Box>
  );
};

export default AnalyticsHome;
